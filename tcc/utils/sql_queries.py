# Consultas SQL
QUERIES = {
    "dProducts": """
        SELECT 
            id AS "idProducts",
            UPPER(name ->> 'pt_BR') AS "ProductDescription"
        FROM product_template pt;
    """,
    "dLoss": """
        SELECT 
            id AS "idLoss",
            UPPER(name ->> 'pt_BR') AS "LossDescription"
        FROM crm_lost_reason;
    """,
    "dContacts": """
        SELECT 
            id AS "idContacts",
            UPPER(name) AS "Name",
            UPPER(street) AS "Address", 
            UPPER(city) AS "City",
            UPPER(REPLACE(SPLIT_PART(tz, '/', 2), '_', ' ')) AS "State"
        FROM res_partner rp;
    """,
    "dStates": """
        SELECT 
            id AS "idStates",
            UPPER(name ->> 'pt_BR') AS "StatesDescription"
        FROM crm_stage cs;
    """,
    "fPipelineCRM": """
        SELECT 
            cl.id AS idCrm,
            cl.date_open::DATE AS DateOpen,
            cl.partner_id AS idContacts,
            cl.stage_id AS idStage,
            cl.priority AS idPriority,
            cl.date_closed::DATE AS DateClosed,
            cl.lost_reason_id AS idLoss,
            cl.description AS Interest,
            so.currency_rate AS qtd_people,
            so.amount_total AS value
        FROM crm_lead cl 
        LEFT JOIN sale_order so ON so.opportunity_id = cl.id;
    """,
}