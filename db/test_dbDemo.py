from API_Calls.configurations import getConnection
import allure
import logging
import utilities.custom_logger as cl

log = cl.customLogger(logging.DEBUG)

@allure.description("Verifying CustomerInfo table and Updating")
def test_getDB():
    conn = getConnection()
    cur = conn.cursor()

    log.info("Selecting CustomerInfo table")
    cur.execute('select * from CustomerInfo')
    rowAll = list(cur.fetchall())
    log.info(rowAll)

    amount_sum = 0

    for r in rowAll:
        amount_sum = amount_sum+r[2]

    log.info("Sum of amount is "+ str(amount_sum))
    assert amount_sum == 340

    log.info("Updating CustomerInfo Table")
    update_query = "update CustomerInfo set Location = %s where CourseName = %s"
    data = ("UK123", "Jmeter")

    cur.execute(update_query,data)
    conn.commit()

    conn.close()