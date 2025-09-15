# TODO

This file tracks actionable items across sessions. New session blocks are appended at the top.

Session: <YYYY-MM-DDTHH:MM:SSZ> # add when update_to_do appends

- [ ] Example task (@priority:medium)
- [ ] Another task (@priority:low)

Session: <previous-session-timestamp>

- [ ] Older task (@priority:high)

Rules:

- Each task is imperative and ≤12 words.
- Use optional inline metadata: @priority, @session.
- Agent should append new session blocks at the top (most recent first).
