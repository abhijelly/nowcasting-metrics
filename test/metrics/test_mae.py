from datetime import datetime
from nowcasting_metrics.metrics.mae import make_mae_one_gsp
from nowcasting_datamodel.models.metric import DatetimeInterval


def test_make_mae(db_session, gsp_yields, forecast_values_latest, datetime_interval):

    value, n = make_mae_one_gsp(session=db_session, datetime_interval=datetime_interval, gsp_id=1)

    assert value == 1.5  # (1-1)*0.5 + (4-1)*0.5
    assert n == 2
