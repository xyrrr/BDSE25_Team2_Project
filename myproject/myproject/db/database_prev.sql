CREATE TABLE `database_prev` (
  `INDEX` int DEFAULT NULL,
  `SK_ID_CURR` int DEFAULT NULL,
  `PREV_ANNUITY_median` double DEFAULT NULL,
  `PREV_APPLICATION_max` double DEFAULT NULL,
  `PREV_CREDIT_max` double DEFAULT NULL,
  `PREV_CREDIT_sum` double DEFAULT NULL,
  `PREV_DOWN_PAYMENT_median` double DEFAULT NULL,
  `PREV_GOODS_PRICE_max` double DEFAULT NULL,
  `PREV_CRE/APP_max` double DEFAULT NULL,
  `RATE_DOWN_PAYMENT_median` double DEFAULT NULL,
  `RATE_INTEREST_PRIMARY_median` double DEFAULT NULL,
  `RATE_INTEREST_PRIMARY_max` double DEFAULT NULL,
  `DAYS_DECISION_median` double DEFAULT NULL,
  `CNT_PAYMENT_median` double DEFAULT NULL,
  `DAYS_PERIOD_median` double DEFAULT NULL,
  `CONTRACT_Cash_loans` double DEFAULT NULL,
  `CONTRACT_Consumer_loans` double DEFAULT NULL,
  `CONTRACT_Revolving_loans` double DEFAULT NULL,
  `Cash through the bank` double DEFAULT NULL,
  `Non-cash from your account` double DEFAULT NULL,
  `PORTFOLIO_Cards` double DEFAULT NULL,
  `PORTFOLIO_Cash` double DEFAULT NULL,
  `PORTFOLIO_POS` double DEFAULT NULL,
  `YIELD_high` double DEFAULT NULL,
  `YIELD_low` double DEFAULT NULL,
  `YIELD_middle` double DEFAULT NULL,
  `HOUR_APPR_PROCESS_START_y` double DEFAULT NULL,
  `WEEKDAY_APPR_PROCESS_START` double DEFAULT NULL,
  `NAME_TYPE_SUITE` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


-- LOAD DATA LOCAL INFILE '/Users/xinyi/Downloads/Database_prev.csv'
-- INTO TABLE database_prev
-- FIELDS TERMINATED BY ',' 
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;