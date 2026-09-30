# Local access for Codex and Claude Code

Git Credential Manager can retain multiple GitHub accounts. This repository selects the sync account locally; other repositories keep their existing settings. Authentication is separate from the commit author identity.

## Set up another computer

Install Git with Git Credential Manager and Python 3. Sign into your normal GitHub account as usual for your other repositories. Then add the sync account without deleting any existing credentials:

```sh
git credential-manager github login --username algorithmsareforsuckers --device
```

Open the displayed GitHub device URL and enter the displayed one-time code. Select algorithmsareforsuckers and review the Git Credential Manager permissions. Do not paste credentials into an agent conversation.

Clone into a separate folder outside any private job-search repository:

```sh
git clone -c credential.username=algorithmsareforsuckers -c credential.https://github.com.username=algorithmsareforsuckers -c credential.helper= -c credential.helper=manager -c user.name=algorithmsareforsuckers -c user.email=336262132+algorithmsareforsuckers@users.noreply.github.com https://algorithmsareforsuckers@github.com/algorithmsareforsuckers/neetcode-submissions.git CodingPractice
cd CodingPractice
python scripts/sync_progress.py
```

The first credential.helper value clears inherited helpers for this checkout only; the second selects Git Credential Manager. This avoids accidentally routing this repository through a different account's CLI helper. No global Git settings are changed.

Run Codex or Claude Code in this folder. Both use the same machine's Git credentials, subject to their tool permissions. Authenticate independently on each machine. In WSL or a container, configure its Git credential manager separately rather than assuming Windows credentials are available there.

## Daily and manual use

NeetCode's accepted-only auto-commit exports future submissions. For a local refresh, run:

```sh
python scripts/sync_progress.py
```

Or ask either agent: "Sync my coding progress now." For submissions not yet exported, open NeetCode's GitHub settings and use accepted-only Bulk Sync, or sync a single submission from its history. Respect the displayed cooldown if rate-limited.

The refresh command refuses a dirty checkout and never overwrites existing work. Original solve dates are absent from native exports; recent commits report sync activity, including backfills.

## Verify identity before a write

```sh
git config --local user.name
git config --local user.email
git remote get-url origin
```

Expected author: algorithmsareforsuckers. Expected email: 336262132+algorithmsareforsuckers@users.noreply.github.com. Use Git in this checkout to push; do not globally switch the main GitHub CLI account merely to work here.
