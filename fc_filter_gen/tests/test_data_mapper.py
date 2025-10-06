import os
import tempfile
import csv
import pytest
from fc_filter_gen.data_mapper import DataMapper

def make_test_csv(contents):
    fd, path = tempfile.mkstemp(suffix='.csv')
    with os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(contents)
    return path

def test_init_loads_players():
    csv_content = "Name,ID\nAlice,1\nBob,2\n"
    path = make_test_csv(csv_content)
    mapper = DataMapper(path)
    assert len(mapper.players) == 2
    assert mapper.players[0]['Name'] == 'Alice'
    assert mapper.players[1]['ID'] == '2'
    os.remove(path)

def test_init_file_not_found():
    with pytest.raises(FileNotFoundError):
        DataMapper('nonexistent.csv')

def test_search_by_name_exact():
    csv_content = "Name,ID\nAlice,1\nBob,2\n"
    path = make_test_csv(csv_content)
    mapper = DataMapper(path)
    result = mapper.search_by_name('Alice')
    assert len(result) == 1
    assert result[0]['Name'] == 'Alice'
    os.remove(path)

def test_search_by_name_case_insensitive():
    csv_content = "Name,ID\nAlice,1\nBob,2\n"
    path = make_test_csv(csv_content)
    mapper = DataMapper(path)
    result = mapper.search_by_name('alice')
    assert len(result) == 1
    assert result[0]['Name'] == 'Alice'
    os.remove(path)

def test_search_by_name_partial():
    csv_content = "Name,ID\nAlice,1\nBob,2\n"
    path = make_test_csv(csv_content)
    mapper = DataMapper(path)
    result = mapper.search_by_name('li')
    assert len(result) == 1
    assert result[0]['Name'] == 'Alice'
    os.remove(path)

def test_search_by_name_no_match():
    csv_content = "Name,ID\nAlice,1\nBob,2\n"
    path = make_test_csv(csv_content)
    mapper = DataMapper(path)
    result = mapper.search_by_name('Charlie')
    assert result == []
    os.remove(path)

def test_search_by_name_empty_csv():
    csv_content = "Name,ID\n"
    path = make_test_csv(csv_content)
    mapper = DataMapper(path)
    result = mapper.search_by_name('Alice')
    assert result == []
    os.remove(path)
