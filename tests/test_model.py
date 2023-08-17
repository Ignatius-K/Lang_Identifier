from model.model import Model

model = Model()


def test_load_model():
    assert model.model is None
    model.load_model('n_bayes_t.pkl')
    assert model.model is not None


def test_detect_language():
    sample_test = {
        'tugenda mu kyalo': 'lug',
        'going to town': 'eng',
    }

    for text in sample_test:
        assert model.detect_language(text) == sample_test[text]
