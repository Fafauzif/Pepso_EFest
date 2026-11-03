# Reverse API Engineer: source inspection and decision for this research run

**Inspected3November2026.** Repository: https://github.com/kalil0321/reverse-api-engineer  
**Pinned commit:** `c644f8af453136ac69489370d6c581d89b9e1bf9`  
**Declared version:**0.14.0  
**Outcome:** cloned and inspected;34Python source files parsed with Python's AST parser without syntax errors. No package installation, upstream runtime, model session, browser capture, generated client or paid call was executed. **Additional observations collected by this tool:0; spend:$0.** This is a scoped capability review, not a security certification or end-to-end test.

## What it actually is

This is a real Python application plus an optional instruction skill, not merely a prompt collection. Its main workflow automates browser traffic capture, supplies that traffic to a configured model/backend, and generates a typed API client. Manual mode records HAR through Playwright; agent modes use Playwright MCP, Chrome DevTools MCP or an agent-browser CLI. Engineer mode regenerates clients from existing captures. The collector implementation delegates collection to a separate Claude Agent SDK loop with web fetch/search and file/shell tools.

The useful transferable method is **observe the website's real public requests, identify the endpoint and pagination schema, replay a small request, then write a bounded source-specific collector**. That is already the method behind our working public endpoint and archive collectors. Installing this application is not necessary to keep doing it in this session.

## What it could add

|Potential benefit|What must exist first|Status in this run|
|---|---|---|
|Capture an unfamiliar dynamic site's public XHR requests|Working browser capture and accessible page|Potentially useful; no such capture tested through this package|
|Save HAR and regenerate a reusable client|A suitable capture plus configured model/backend|Not executed|
|Generate typed clients in several languages|External runtime/model access and later code review|No extra benefit for the present Python CSV/JSON research workflow|
|Autonomous generic web collection|A separately configured SDK/model and tools|Overlaps the tools and reasoning already available here|
|Reuse the user's existing Chrome session|Headed Chrome connection and permission/session access|Not used; not needed for public-data routes|

The project does not create access to a private API by itself. A generated client inherits any authentication, expiry, location, rate, pagination and source-availability limits in the captured requests. A blocked or unavailable source remains blocked or unavailable unless an independently supported public route exists.

## Source observations that affect execution

- `pyproject.toml` declares21core dependencies, including a Claude Agent SDK, HTTP libraries, CLI/UI libraries and cryptography. Manual mode adds Playwright and playwright-stealth; collector extras add parsing libraries.
- `src/reverse_api/collector.py` configures a Claude SDK client with Read/Write/Bash/WebFetch/WebSearch and `permission_mode="bypassPermissions"` around lines104–116. The package's own permission setting does not override this session's authority or safety boundaries.
- `src/reverse_api/auto_engineer.py` builds `npx`-launched browser MCP configurations; default Chrome mode can attach to an existing session, while headless options start without those sessions. Some configurations use a package specifier ending in`@latest`; execution should pin versions.
- `src/reverse_api/agent_browser.py` can run a global`npm install -g` when the binary is absent, with an`npx`fallback. The command is not a read-only diagnostic and was not executed here.
- `src/reverse_api/browser.py` contains browser-fingerprint/stealth adjustments. Those are not a guarantee of access, and they were not used as a way around any restriction.
- `src/reverse_api/engineer.py` starts a separate model-backed generation session; generated scripts need inspection before execution.
- The upstream README describes multiple backends and session configurations. This ChatGPT conversation's model access is not automatically a credential for those external SDKs or model services. No private configuration or authentication files were inspected to find a workaround.
- HAR traffic may contain cookies, tokens or personal request data. No such captures were made, copied or committed during this audit.

## Actual local checks

The checkout succeeded outside the project repository, at a scratch audit path. The metadata file records commit, inspected source hashes and declared dependencies. An isolated availability check found no `claude_agent_sdk`, `click`, `rich`, `requests` or`playwright` in the Python interpreter used for this audit. That describes this interpreter, not every possible runtime on the host.

All34Python source files passed `ast.parse`. This checks syntax without importing or executing the upstream application. It does not verify dependencies, runtime behavior, credential handling, extraction accuracy or source access.

No narrow runtime test was selected: the working ArcticShift/retailer routes already expose their endpoint shapes directly, so a nested model/browser installation would add setup and unverified external dependencies without a specific collection gap it demonstrably resolves. The autonomous next step remains to adapt the useful public-request inspection method using the tools already available, rather than ask the user to configure this package.

## Practical decision

**Keep the technique; do not make this package a dependency of the research release.** It is a credible candidate when an accessible dynamic page has an unknown request flow and preserving a reusable client is worth the additional runtime. It is not evidence that millions of relevant reviews are now reachable, and it should not be credited with data it never collected.

The saved files `reverse_api_engineer_metadata.json`, `reverse_api_engineer_README_snapshot.md` and `reverse_api_engineer_pyproject_snapshot.toml` distinguish what was actually inspected from upstream promises. No upstream executable code was vendored into the research repository. The full checkout remains outside the project in scratch.
