# FASTA Reader

Библиотека на Python для чтения последовательностей в формате FASTA.

## Возможности

- **Класс `Seq`** — хранит последовательность и её заголовок.
- **Класс `FastaReader`** — читает FASTA-файл по записям через генератор.
- **Оптимизация** — файл читается построчно, весь файл не загружается в память.
- **Определение типа** — автоматически определяет нуклеотид или белок.

## Установка

```bash
git clone https://github.com/SonyaShust/FastaReader.git
cd FastaReader
```

## Использование

```python
from lib import FastaReader

reader = FastaReader("code1.fasta")

for seq in reader.read():
    print(seq)
    print(f"Длина: {len(seq)}")
    print(seq.getalphabet())
```

## Запуск демонстрации

```bash
python3 demo.py
```

Программа спросит путь к FASTA-файлу. введите название файла

```
code1.fasta
```

## Документация

Собранная HTML-документация лежит в `docs/_build/html/`.


## Примеры файлов

- `code1.fasta`
- `code2.fasta`

