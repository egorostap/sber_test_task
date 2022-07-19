from funcs import *

'''
для выплонения заданий и тестов была сформирована база данных согласно требованиям в заданиях, прилагаю ее в репозитории
функции обработки запросов прописал в файле "funcs"
'''

task_1 = '''
SELECT Transactions.Client_id, Transactions.Report_date, 
round(Transactions.Txn_amount/
(
SELECT 
case 
when Transactions.Report_date in (SELECT Rates.Report_date FROM Rates)
then (SELECT Rates.CCy_rate FROM Rates WHERE Transactions.Report_date = Rates.Report_date)
else (SELECT Rates.CCy_rate FROM Rates WHERE Transactions.Report_date > Rates.Report_date ORDER BY Rates.Report_date desc limit 1)
end
FROM Rates 
)
, 2) as Amount_USD
FROM Transactions
'''

task_2 = '''
WITH t_id_vsp_mx_dt_mnth AS
(
SELECT Client_id, VSP_Number, max(Report_date) as max_rep_date, CAST(strftime('%m', max(Report_date)) AS INTEGER) as month FROM VSP_oper_data GROUP BY Client_id, strftime('%m', Report_date)
)

SELECT VSP_oper_data.Client_id, strftime('%m', VSP_oper_data.Report_date) as Report_date,

(SELECT sum(VSP.Txn_amount) FROM VSP_oper_data VSP WHERE VSP.Txn_type="debit" and VSP.Client_id = VSP_oper_data.Client_id AND strftime('%m', VSP.Report_date) = strftime('%m', VSP_oper_data.Report_date)) 
as Debit_amount,

(SELECT sum(VSP.Txn_amount) FROM VSP_oper_data VSP WHERE VSP.Txn_type="credit" and VSP.Client_id = VSP_oper_data.Client_id AND strftime('%m', VSP.Report_date) = strftime('%m', VSP_oper_data.Report_date)) 
as Credit_amount,

(SELECT t_id_vsp_mx_dt_mnth.VSP_Number FROM t_id_vsp_mx_dt_mnth WHERE t_id_vsp_mx_dt_mnth.Client_id = VSP_oper_data.Client_id AND t_id_vsp_mx_dt_mnth.month = strftime('%m', VSP_oper_data.Report_date)) 
as Last_VSP

FROM VSP_oper_data
GROUP BY VSP_oper_data.Client_id, strftime('%m', VSP_oper_data.Report_date)
'''

task_3 = '''
WITH month_month_amount AS
(
SELECT CAST(strftime('%m', Report_date) AS INTEGER) as month, CAST(SUM(Txn_amount) AS REAL) as month_amount FROM VSP_oper_data  WHERE Txn_type='debit' GROUP BY strftime('%m', Report_date)
)

SELECT Client_id, CAST(strftime('%m', Report_date) AS INTEGER) AS Report_date, 
ROUND(SUM(Txn_amount)/(SELECT month_amount FROM month_month_amount WHERE month = strftime('%m', VSP_oper_data.Report_date)),4) as Ratio
FROM VSP_oper_data 
WHERE Txn_type='debit'
GROUP BY Client_id, strftime('%m', Report_date)
'''


task_4 = '''
WITH AB AS
(
SELECT VSP, VAL, GROUP_VSP
FROM distance_metric
),
BA AS 
(
SELECT VSP_E, VAL, GROUP_VSP
FROM distance_metric
)
SELECT VSP, min(VAL) as MIN_VAL, round(sum(VAL)/count(VAL), 1) as AVG_VAL, max(VAL) as MAX_VAL, GROUP_VSP
FROM
(SELECT VSP, VAL, GROUP_VSP FROM AB
union all
SELECT VSP_E as VSP, VAL, GROUP_VSP FROM BA) DATA
GROUP BY GROUP_VSP, VSP
'''

# сделать корректно не удалось, в sqlite нет возмжоности задавать переменные, другого способа не нашел
task_5 = '''
SELECT 
USER_ID, user_position,
MIN(date_position) OVER (PARTITION BY user_position) AS position_start,
MAX(date_position) OVER (PARTITION BY user_position) AS position_end
FROM users_position
ORDER BY USER_ID, position_start
'''

# Запуск функции
if __name__ == '__main__':
    # pass
    
    # task_1
    print(input_base(sql_request=task_1, base_name='sber_data.sqlite3'))
    print()
    # task_2
    print(input_base(sql_request=task_2, base_name='sber_data.sqlite3'))
    print()
    # task_3
    print(input_base(sql_request=task_3, base_name='sber_data.sqlite3'))
    print()
    # task_4
    print(input_base(sql_request=task_4, base_name='sber_data.sqlite3'))
    print()
    # task_5
    # print(input_base(sql_request=task_5, base_name='sber_data.sqlite3'))