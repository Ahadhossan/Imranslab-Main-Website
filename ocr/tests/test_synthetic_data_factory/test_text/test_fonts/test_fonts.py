import pytest
from test_data.synthetic_data.synthetic_data_factory.text.fonts.fonts import FontLibrary


@pytest.fixture
def font_library():
    return FontLibrary()


@pytest.mark.sanity
def test_fonts_is_list(font_library):
    fonts = font_library.get_all_fonts()
    assert isinstance(fonts, list), "Fonts should be a list"


@pytest.mark.sanity
def test_fonts_not_empty(font_library):
    fonts = font_library.get_all_fonts()
    assert len(fonts) > 0, "Fonts list should not be empty"


@pytest.mark.sanity
@pytest.mark.edgecase
def test_all_fonts_are_strings(font_library):
    fonts = font_library.get_all_fonts()
    for font in fonts:
        assert isinstance(font, str), f"Font '{font}' should be a string"


@pytest.mark.sanity
@pytest.mark.edgecase
def test_no_empty_font_names(font_library):
    fonts = font_library.get_all_fonts()
    for font in fonts:
        assert font.strip() != "", "Font name should not be empty"


@pytest.mark.edgecase
def test_get_font_valid_indices(font_library):
    fonts = font_library.get_all_fonts()
    for i in range(len(fonts)):
        assert font_library.get_font(i) == fonts[i]


@pytest.mark.edgecase
def test_get_font_negative_index(font_library):
    fonts = font_library.get_all_fonts()
    # Should support negative indexing like a normal list
    assert font_library.get_font(-1) == fonts[-1]
    assert font_library.get_font(-2) == fonts[-2]


@pytest.mark.edgecase
def test_get_font_out_of_range(font_library):
    fonts = font_library.get_all_fonts()
    with pytest.raises(IndexError):
        font_library.get_font(len(fonts))
    with pytest.raises(IndexError):
        font_library.get_font(-len(fonts) - 1)


@pytest.mark.performance
def test_fonts_list_performance(font_library, benchmark):
    # Benchmark access to all fonts
    benchmark(font_library.get_all_fonts)
