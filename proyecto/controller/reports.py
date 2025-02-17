from config.app import *
import pandas as pd

def GenerateReportVentas(app:App):
    conn=app.bd.getConection()
    query="""
            SELECT  
                v.order_id,
                f.order_date, 
                f.ship_date,
                v.profit
            FROM 
                FECHA AS f
            INNER JOIN 
                VENTAS AS v ON v.order_id = f.order_id
            GROUP BY 
                f.order_id, f.order_date, f.ship_date
            HAVING 
                CAST(v.profit AS REAL) > 500;
    """
    df=pd.read_sql_query(query,conn)
    path="/workspaces/workspacepy01/proyecto/files/Reporte.csv"
    df.to_csv(path)
    sendMail(app,path)

def sendMail(app:App,Reporte):
    app.mail.send_email('from@example.com','Marquina Huaman Alan Fernando Martin','Reporte de ganancias mayores a 500 agrupadas por order_id y fecha',Reporte)