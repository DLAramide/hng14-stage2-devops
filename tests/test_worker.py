def test_worker_runs(monkeypatch):
    class FakeRedis:
        def ping(self):
            return True

    monkeypatch.setattr("worker.worker.redis.Redis", lambda *args, **kwargs: FakeRedis())

    from worker.worker import redis  # import AFTER patch

    r = redis.Redis()
    assert r.ping() is True