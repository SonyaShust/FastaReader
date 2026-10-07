"""
Модуль для работы с последовательностями в формате FASTA.

Содержит два класса:
    - Seq: хранит одну последовательность и её заголовок.
    - FastaReader: читает FASTA-файл и возвращает объекты Seq.
"""


class Seq:
    """
    Класс для хранения одной биологической последовательности.

    Атрибуты:
        header (str):   Заголовок записи (без символа '>').
        sequence (str): Сама последовательность (ДНК, РНК или белок).
    """

    def __init__(self, header, sequence):
        """
        Создаёт объект последовательности.

        Аргументы:
            header (str):   Название/описание записи.
            sequence (str): Строка с символами последовательности.
        """
        self.header = header
        self.sequence = sequence

    def __str__(self):
        """
        Возвращает строковое представление в формате FASTA.

        Возвращает:
            str: Запись в виде '>заголовок\\nпоследовательность'.
        """
        return f">{self.header}\n{self.sequence}"

    def __len__(self):
        """
        Возвращает длину последовательности.

        Возвращает:
            int: Количество символов в последовательности.
        """
        return len(self.sequence)

    def getalphabet(self):
        """
        Определяет тип последовательности.

        Возвращает:
            str: 'Alphabet: Nucleotide', 'Alphabet: Protein'
                 или 'Unknown alphabet'.
        """
        seq = set(self.sequence.upper())
        N = set("ATGUC")
        P = set("ACDEFGHIKLMNPQRSTVWY")

        if seq.issubset(N):
            return "Alphabet: Nucleotide"
        elif seq.issubset(P):
            return "Alphabet: Protein"
        else:
            return "Unknown alphabet"


class FastaReader:
    """
    Класс для чтения файла в формате FASTA.

    Возвращает отдельные объекты Seq по мере чтения файла.
    Использует генератор, поэтому весь файл не загружается в память.
    """

    def __init__(self, filepath):
        """
        Создаёт читатель для указанного файла.

        Аргументы:
            filepath (str): Путь к FASTA-файлу.

        Исключения:
            FileNotFoundError: Если файл не найден.
            ValueError:        Если файл не соответствует формату FASTA.
        """
        self.filepath = filepath
        try:
            with open(filepath, "r") as file1:
                first_char = file1.read(1)
                if first_char != ">":
                    raise ValueError(f"File {filepath} is not in Fasta format")
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filepath} is not exist")

    def read(self):
        """
        Генератор, который по одной отдаёт записи из файла.

        Yields:
            Seq: очередная последовательность из файла.
        """
        with open(self.filepath, "r") as file2:
            header = None
            parts = []

            for line in file2:
                line = line.strip()

                if not line:
                    continue

                if line.startswith(">"):
                    if header is not None:
                        yield Seq(header, "".join(parts))
                    header = line[1:]
                    parts = []
                else:
                    parts.append(line)

            if header is not None:
                yield Seq(header, "".join(parts))
