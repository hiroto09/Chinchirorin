from flask import Blueprint, render_template, request, redirect, url_for
from models import Record

# Blueprintの作成
records_bp = Blueprint('records', __name__, url_prefix='/records')

@records_bp.route('/')
def index():

    # データ取得
    record_list = Record.select()

    records = []
    for record in record_list:
        records.insert(0, {
            "name": record.name,
            "isWin": record.isWin,
            "playerDice": record.playerDice,
            "cpuDice": record.cpuDice,
        })
    
    return render_template('records.html',records=records)