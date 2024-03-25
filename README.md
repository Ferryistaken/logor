Let's streamline the README to focus on simplicity, elegance, and the essence of **Loquor**. We'll cut down on the fluff and make sure each word carries its weight.

---

# Loquor 🗣️

**Loquor** elegantly bridges Git repositories and Language Learning Models (LLMs), offering a simple tool for extracting and preparing your code for LLM interactions.

## Features 🚀

- **Customizable Filtering**: Effortlessly include or exclude specific file types with `-i` and `-e` flags.
- **Elegance in Execution**: Loquor is designed with a focus on simplicity, making powerful operations accessible to everyone.
- **Open-Source Spirit**: Dive in, tailor Loquor to your needs, and contribute your enhancements back to the community.

## Quick Start 🌟

### Setup

Make sure Git and Python are installed on your machine.

```bash
git clone https://github.com/Ferryistaken/loquor.git
cd Loquor
```

## Flags 🚩

Loquor supports several flags to tailor its operation to your needs. Below is a table describing each flag:

| Flag | Description                                                                 | Example                |
|------|-----------------------------------------------------------------------------|------------------------|
| `-i` | Include files matching this pattern. Can be used multiple times.            | `-i *.py` (include Python files) |
| `-e` | Exclude files matching this pattern. Can be used multiple times.            | `-e *.bin` (exclude binary files) |
| `-c` | Copy the output directly to the clipboard. Useful for immediate use.        | `-c` (copy output to clipboard)   |

### Command Line Usage

Customize Loquor's functionality with the flags according to your project's needs:

**Include Python and Markdown Files:**

```bash
python loquor.py -i *.py -i *.md
```

**Exclude Binary Files and Copy to Clipboard:**

```bash
python loquor.py -i * -e *.bin -c
```


## Examples 📘

**Just Python Files:**

```bash
python loquor.py -i *.py
```

**Exclude Binary and Temporary Files:**

```bash
python loquor.py -i * -e *.bin -e *~
```

## License 📄

Loquor is licensed under the MIT License. For more details, see the LICENSE file.

