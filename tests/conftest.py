import vcr

my_vcr = vcr.VCR(
    path_transformer=vcr.VCR.ensure_suffix('.yaml'),
    cassette_library_dir='fixtures/cassettes',
    record_mode='once',
    match_on=['uri', 'method'],
)
