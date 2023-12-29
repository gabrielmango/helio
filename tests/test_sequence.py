from helio import Sequence

def test_return_main():
    table_name_1 = 'tb_testing'
    table_name_2 = 'tb_testing_helio'
    sequence_name_1 = Sequence.main(table_name_1)
    sequence_name_2 = Sequence.main(table_name_2)


    assert sequence_name_1 == 'sq_testing_coseqt'
    assert sequence_name_2 == 'sq_testinghelio_coseqth'