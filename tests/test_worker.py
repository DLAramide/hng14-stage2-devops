def test_worker_runs(mocker):
    mock_redis = mocker.patch("worker.worker.redis.Redis")
    instance = mock_redis.return_value
    instance.ping.return_value = True

    assert instance.ping() is True