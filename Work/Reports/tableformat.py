from stock import Stock

class FormatError(Exception):
    pass

class TableFormatter:
    def headings(self, headers: list[str] | tuple[str, ...]) -> None:
        '''Emit the table headings'''
        raise NotImplementedError()
    
    def row(self, rowdata: list[str] | tuple[str, ...]) -> None:
        '''Emit a single row of table data'''
        raise NotImplementedError()
    
class TextTableFormatter(TableFormatter):
    '''Emit a table in plain-text format'''
    def headings(self, headers):
        print(' '.join(f'{h.capitalize():>10s}' for h in headers))
        print(('-'*10 + ' ') * len(headers))

    def row(self, rowdata):
        print(' '.join(f'{entry:10s}' for entry in rowdata))

class CSVTableFormatter(TableFormatter):
    '''Output portfolio data in csv format'''
    def headings(self, headers): 
        print(','.join(h.capitalize() for h in headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''Output portfolio data in HTML table format'''
    def headings(self, headers):
        print('<tr>', end='')
        print(''.join(f'<th>{h.capitalize()}</th>' for h in headers), end='')
        print('</tr>')
    
    def row(self, rowdata):
        print('<tr>', end='')
        print(''.join(f'<th>{entry}</th>' for entry in rowdata), end='')
        print('</tr>')


def create_formatter(format: str) -> TableFormatter:
    '''Creates an instance of class for provided format, including "txt", "csv" and "html"'''
    if format == 'txt':
        return TextTableFormatter()
    elif format == 'csv':
        return CSVTableFormatter()
    elif format == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f"Can't use format {format!r}. Try 'txt', 'csv' or 'html'.")
    
def print_table(portfolio: list[Stock], formatter: TableFormatter, select: list[str] = ['name', 'shares', 'price']) -> None:
    formatter.headings(select)    
    
    for entry in portfolio:
        entry = tuple(str(getattr(entry, colname)) for colname in select)
        formatter.row(entry)