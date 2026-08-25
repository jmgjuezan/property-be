from datetime import datetime, timezone


def format_db_date(model, fields):
    for field in fields:
        if model.get(field, None) is not None:
            model[field] = datetime(
                model[field].year,
                model[field].month,
                model[field].day,
                tzinfo=timezone.utc
            )
    return model


def format_ui_date(model, fields):
    for field in fields:
        if model.get(field, None) is not None:
            model[field] = model[field].date()
    return model
