#!/usr/bin/env python3
"""AI 产品拆解项目初始化脚本（Windows / macOS / Linux 通用）。

用法:
    python init_project.py "产品名称"      # Windows
    python3 init_project.py "产品名称"     # macOS / Linux
"""

import sys
from pathlib import Path


def _safe_stdout() -> None:
    """Windows 控制台默认 GBK，统一转成 UTF-8，避免中文/符号报错。"""
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def desktop_dir() -> Path:
    home = Path.home()
    for candidate in (home / "Desktop", home / "OneDrive" / "Desktop"):
        if candidate.is_dir():
            return candidate
    return home / "Desktop"


def main() -> int:
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print('用法: python init_project.py "产品名称"')
        return 1

    product_name = sys.argv[1].strip()
    project_dir = desktop_dir() / f"{product_name}_拆解"

    if project_dir.exists():
        print(f"[WARN] 项目文件夹已存在：{project_dir}")
        print("如需重新初始化，请先删除或重命名现有文件夹。")
        return 1

    project_dir.mkdir(parents=True, exist_ok=True)

    print(f"[OK] 项目文件夹已创建：{project_dir}")
    print()
    print("[FILES] 文件结构：")
    print(f"  {product_name}_拆解/")
    for name, note in [
        ("00_拆解概览.md", ""),
        ("01_市场层.md", " (待创建)"),
        ("02_商业层.md", " (待创建)"),
        ("03_用户层.md", " (待创建)"),
        ("04_技术层.md", " (待创建)"),
        ("05_模型层.md", " (待创建)"),
        ("06_基础层.md", " (待创建)"),
        ("07_总结与架构图.md", " (待创建)"),
    ]:
        print(f"  +-- {name}{note}")
    return 0


if __name__ == "__main__":
    _safe_stdout()
    raise SystemExit(main())
