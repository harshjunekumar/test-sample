"""Step 3: The chatbot.

A command-line chat with Claude that answers questions about customer personas.
Claude decides which tools to call (see persona_tools.py), this script runs
them, and Claude answers from the results.

The tool loop is written out by hand so you can see exactly how it works:
  1. Send the conversation + tool definitions to Claude
  2. If Claude asks for tools (stop_reason == "tool_use"), run them and send the results back
  3. Repeat until Claude gives a final answer (stop_reason == "end_turn")

Run: python chatbot.py         (needs ANTHROPIC_API_KEY set)
"""
import anthropic

from persona_tools import TOOLS, run_tool

MODEL = "claude-opus-5-5"

SYSTEM_PROMPT = """You are a customer-insights analyst for an e-commerce company. You help \
product, marketing and category teams understand the company's customer personas.

The personas were built by clustering 6,000 customers on their buying behaviour \
(order frequency, basket value, recency, discount use, returns, holiday buying and category mix). \
Use the tools to look up facts; never invent numbers. If the data can't answer a question, say so \
and suggest what data would.

When you answer:
- Lead with the insight, then the supporting numbers.
- Turn findings into practical actions (offers, messaging, merchandising, experiments to run).
- Keep it concise. Use a small table when comparing personas.
- Mention that the data is synthetic if someone asks about real-world customers."""


def ask(client: anthropic.Anthropic, messages: list) -> None:
    """Run one user turn: call Claude, run any tools it asks for, print the answer."""
    while True:
        response = client.beta.messages.create(
            model=MODEL,
            max_tokens=16000,
            system=SYSTEM_PROMPT,
            tools=TOOLS,
            messages=messages,
            output_config={"effort": "medium"},
            # If a safety check declines a request, retry it on a suitable fallback model
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
        )
        # Keep the full response (not just its text) so the conversation history stays valid
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "refusal":
            print("\nAssistant: Sorry, I can't help with that request.\n")
            return
        if response.stop_reason != "tool_use":
            text = "".join(b.text for b in response.content if b.type == "text")
            if response.stop_reason == "max_tokens":
                text += "\n[Answer cut off: hit the max_tokens limit]"
            print(f"\nAssistant: {text}\n")
            return

        # Claude asked for one or more tools: run them all, send every result back in one message
        results = []
        for block in response.content:
            if block.type == "tool_use":
                print(f"  [tool] {block.name}({block.input})")
                output, is_error = run_tool(block.name, block.input)
                results.append({"type": "tool_result", "tool_use_id": block.id,
                                "content": output, "is_error": is_error})
        messages.append({"role": "user", "content": results})


def main() -> None:
    client = anthropic.Anthropic()
    messages = []
    print("Persona Insights Chatbot. Ask about your customer personas (type 'quit' to exit).")
    print("Try: 'Which persona should we target for a Diwali campaign, and why?'\n")
    while True:
        try:
            question = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if question.lower() in {"quit", "exit"}:
            break
        if not question:
            continue
        messages.append({"role": "user", "content": question})
        try:
            ask(client, messages)
        except anthropic.AuthenticationError:
            print("Authentication failed: set ANTHROPIC_API_KEY to a valid key.")
            break
        except anthropic.RateLimitError:
            print("Rate limited. Wait a moment and try again.")
            messages.pop()
        except anthropic.APIConnectionError:
            print("Network error: check your internet connection.")
            messages.pop()


if __name__ == "__main__":
    main()
