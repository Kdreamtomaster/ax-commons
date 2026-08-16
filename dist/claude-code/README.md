# Claude Code

`~/.claude/skills/` 에 이 폴더 안의 두 폴더를 그대로 복사한다.

```bash
mkdir -p ~/.claude/skills
cp -r owner-lens insight-commons ~/.claude/skills/
```

윈도우(PowerShell):

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item owner-lens,insight-commons "$env:USERPROFILE\.claude\skills\" -Recurse -Force
```

특정 프로젝트에서만 쓰려면 `~/.claude/skills` 대신 그 프로젝트의
`.claude/skills/` 에 넣는다.

확인: `claude` 실행 후 `/owner-lens`

※ 이 폴더는 자동 생성된다. 고치려면 `skills/` 를 고치고 `python3 scripts/build.py`.
