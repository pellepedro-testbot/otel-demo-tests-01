import pytest


def test_put_currency_answers_405_with_allow_get_and_empty_body(api):
    resp = api.request("PUT", "/api/currency", timeout=5)
    assert resp.status_code == 405
    assert resp.headers["Allow"] == "GET"
    assert resp.content == b""
    assert resp.elapsed.total_seconds() < 5


@pytest.mark.parametrize("method", ["POST", "DELETE", "PATCH"])
def test_other_unhandled_methods_on_currency_answer_like_put(api, method):
    put = api.request("PUT", "/api/currency", timeout=5)
    resp = api.request(method, "/api/currency", timeout=5)
    assert resp.status_code == 405
    assert resp.headers["Allow"] == "GET"
    assert resp.content == b""
    assert resp.elapsed.total_seconds() < 5
    assert (resp.status_code, resp.headers.get("Allow")) == (put.status_code, put.headers.get("Allow"))
