# Agent instructions

This is a public repository of accepted NeetCode submissions, automatically populated by NeetCode. Use it to understand coding practice, not as a place for private coaching or job-search records.

## Read and refresh

- Before progress reviews or problem recommendations, run `python scripts/sync_progress.py` from this repository. This pulls with `--ff-only` and reports the currently tracked problems. If Python is unavailable, use `git pull --ff-only`, inspect solution paths, and read `git log`.
- For "sync my coding progress now", run that same command. It refreshes solutions already exported by NeetCode. If an accepted submission is missing, use NeetCode GitHub settings or its submission-history sync control; a Git pull cannot force the source site to export.
- Count unique problem paths separately from submission files and languages. Only accepted submissions are configured for export. Missing files do not prove an unsolved problem, especially while backfill is incomplete.
- Native solution files do not include original submission timestamps. Git commit dates are sync dates, not verified solve dates. Historical bulk imports must never count as problems solved that day. Use separately verified submission metadata where available and label unknown dates honestly.
- Acceptance alone does not establish independent mastery, time spent, or whether hints were used.

## Write access and privacy

- Authenticate Git operations as `algorithmsareforsuckers`. Use repo-local user.name `algorithmsareforsuckers` and user.email `336262132+algorithmsareforsuckers@users.noreply.github.com`.
- Do not change global Git identity or switch the default GitHub CLI account. The CLI and Git credentials can differ. Use this checkout's configured Git for pushes; a GitHub connector authenticated as another account may be read-only here.
- Never add personal names, personal email addresses, private coaching notes, job-search data, local user paths, or credentials to this public repository. Keep private context in its private project.
- Preserve native submission files as evidence. Put explanations or alternative solutions in separate files. Do not fabricate submissions or mark agent-written code as the user's completed work.
- Stage only intended files. Before pushing, fetch and rebase your own new commits onto origin/main if needed; NeetCode may push concurrently. Never force-push, discard user changes, or delete submission history.
- If the checkout is dirty, finish or preserve the existing work before refreshing. Never stash or reset another agent's work automatically.

## Setup

Read `docs/LOCAL_SETUP.md` when configuring another computer. Every machine authenticates independently; no tokens or private keys belong in this repository.
