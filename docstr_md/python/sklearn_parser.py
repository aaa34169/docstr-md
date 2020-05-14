import ast
import re


class SklearnParser():        
    def parse(self, obj, select_names=('Notes', 'Examples')):
        docstr = {'description': '', 'sections': [], 'fields': []}
        if not (isinstance(obj, ast.Expr) and obj.value.s):
            return docstr
        section_names, sections = self.get_sections(obj.value.s)
        docstr['description'] = self.parse_lines(sections.pop(0))
        docstr['sections'] = [
            self.parse_section(name, section_names, sections)
            for name in select_names if name in section_names
        ]
        docstr['fields'] = [
            self.parse_field(name, section) 
            for name, section in zip(section_names, sections) 
        ]
        return docstr

    def get_sections(self, docstr_txt):
        sections = re.split('\n\s+-+\n', docstr_txt)
        sections = [section.splitlines() for section in sections]
        sections = [
            [line.strip() for line in section] for section in sections
        ]
        section_names = [sections[i-1].pop() for i in range(1, len(sections))]
        return section_names, sections 
        
    def parse_lines(self, lines):
        return ''.join(['\n'+line for line in lines]).strip()

    def parse_section(self, name, section_names, sections):
        idx = section_names.index(name)
        section_names.pop(idx)
        content = self.parse_lines(sections.pop(idx))
        return (name, content)   

    def parse_field(self, name, lines):
        field = {'name': name}
        idx_list = [idx for idx, val in enumerate(lines) if val == '']
        idx_list = zip([-1]+idx_list[:-1], idx_list)
        field['items'] = [
            self.parse_item(name, lines[i+1:j]) 
            for i, j in idx_list
        ]
        return field

    def parse_item(self, name, lines):
        item = {}
        head = lines.pop(0).split(':', maxsplit=2)
        name, short_desc = head if len(head) == 2 else (head[0], '')
        item['name'], item['short_desc'] = name.strip(), short_desc.strip()
        item['long_desc'] = ' '.join(lines)
        return item