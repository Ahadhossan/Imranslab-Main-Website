class FontLibrary:
    def __init__(self):
        self.fonts = [
            'Times New Roman',
            'Arial',
            'Arial Black',
            'Comic Sans MS',
            'Courier New',
            'Georgia',
            'Impact',
            'Lucida Console',
            'Palatino Linotype',
            'Tahoma',
            'Trebuchet MS',
            'Verdana',
            'Wingdings',
            'Arial Narrow',
            'Book Antiqua',
        ]

    def get_font(self, index=0):
        return self.fonts[index]

    def get_all_fonts(self):
        return self.fonts

# Example usage
if __name__ == "__main__":
    font_library = FontLibrary()
    print(font_library.get_font(0))