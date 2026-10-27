# -*- coding: utf-8 -*-
"""把 chapters/ 中指定章节正文同步回 notes-personal/正文草稿.md（仅勘误通道）"""
import re
import sys
import glob
import os

# [HISTORICAL BURDEN — removed 2026-10] Two legacy smells fixed here:
#   1. `sys.stdout.reconfigure(encoding='utf-8')` ran at *import time*, mutating
#      global state on a mere import. UTF-8 output is now enabled explicitly in
#      main().
#   2. The whole script body ran at module scope, so importing this file (e.g. in
#      a test or another script) would execute the sync. Logic now lives in
#      main(); the file is import-safe.
# sys.stdout.reconfigure(encoding='utf-8')


def _enable_utf8_console() -> None:
    """Best-effort UTF-8 stdout. Guarded so captured/non-CPython streams no-op."""
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
    except (ValueError, OSError):
        pass


DRAFT = 'notes-personal/正文草稿.md'


def main(argv=None) -> int:
    nums = list(argv if argv is not None else sys.argv[1:]) or ['042', '028', '030', '033', '037']

    src = {}
    for p in glob.glob('chapters/**/*.md', recursive=True):
        m = re.search(r'第(\d+)章', os.path.basename(p))
        if m:
            src[str(int(m.group(1)))] = p

    t = open(DRAFT, encoding='utf-8').read()
    lines = t.split('\n')

    for n in nums:
        key = str(int(n))
        if key not in src:
            print('缺少章节文件', n)
            continue
        body = open(src[key], encoding='utf-8').read().strip('\n')
        pat = re.compile(r'^## 第0*' + str(int(n)) + r'章')
        start = next((i for i, ln in enumerate(lines) if pat.match(ln)), None)
        if start is None:
            print('草稿中未找到 第%s章' % n)
            continue
        end = len(lines)
        for j in range(start + 1, len(lines)):
            if re.match(r'^## 第\d+章', lines[j]) or re.match(r'^# ', lines[j]):
                end = j
                break
        lines[start:end] = body.split('\n') + ['']
        print('同步 第%s章 -> 草稿' % n)

    # 落盘一律 LF（与 scan_hygiene.py 的硬性规则一致）
    open(DRAFT, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines))

    # 校验：章标题零差异
    d = set(re.findall(r'^## 第(\d+)章 (.+)$', '\n'.join(lines), re.M))
    c = set()
    for k, p in src.items():
        m = re.search(r'^## 第(\d+)章 (.+)$', open(p, encoding='utf-8').read(), re.M)
        if m:
            c.add((m.group(1), m.group(2)))
    print('草稿章数', len(d), 'chapters 章数', len(c), '标题差异', len(d ^ c))
    return 0


if __name__ == '__main__':
    _enable_utf8_console()
    sys.exit(main())
