from .date_helper import format_db_date, format_ui_date

def format_db_fields(model, fields):
    model = format_db_date(model, fields)
    clean_model = {k: v for k, v in model.items() if v is not None}
    return clean_model

def format_ui_fields(models, fields):
    model_list = list(models)
    for index, model in enumerate(model_list):
        model_list[index] = format_ui_field(model, fields)
    return model_list

def format_ui_field(model, fields):
    model["_id"] = str(model["_id"])
    model = format_ui_date(model, fields)
    return model
