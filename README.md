IMPORTANT NOTE (READ THIS FIRST)

This project is intentionally designed to send ONLY SINGLE-LINE WhatsApp messages.

WhatsApp Web behaves inconsistently under automation when handling multiline input
(\n, SHIFT+ENTER, or pasted line breaks). Attempting multiline messages can result in:
- Partial sends
- Draft corruption
- Messages not being sent
- Stale DOM errors

To ensure reliability:
- Message content MUST be single-line
- Line breaks are not supported
- Use spaces or separators (e.g. " | ") instead of newlines

This constraint is not a limitation of the agent design, but a known instability of
WhatsApp Web’s UI when automated.

Following this rule guarantees:
- Deterministic behavior
- Clean sends
- No draft-related bugs
- No partial or failed messages
