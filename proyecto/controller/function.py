from sqlite3 import Connection
import pandas as pd

#importacion como si se llamara desde el archivo principal
from config.app import *
from modelos.model import *

def IngestDataProducts(app:App):
    bd=app.bd
    conn=bd.getConection()
    dataCategories=GetDataSourceCategories()
    createTableCategories(conn)
    InsertManyCategories(bd,dataCategories)
    dataProducts=GetDataSourceProductos(conn)
    createTableProducts(conn)
    InsertManyProducts(bd,dataProducts)
    dataVentas=GetDatasourceOrders(conn)
    createTableVentas(conn)
    insertManyVentas(bd,dataVentas)
    datafecha=GetDatasourceFecha()
    createTableFecha(conn)
    InsertManyFecha(bd,datafecha)


def GetDataSourceCategories():
    pathData="/workspaces/workspacepy01/proyecto/files/data.xls"
    df=pd.read_excel(pathData,sheet_name="Orders")
    df_categories=df[['Category','Sub-Category']].dropna().drop_duplicates()
    categories_tuples=[tuple(x) for x in df_categories.to_records(index=False)]
    return categories_tuples

def createTableCategories(conn:Connection):
    categories=Categorias()
    categories.create_table(conn)

def InsertManyCategories(bd:Database,data):
    bd.insert_many('CATEGORIAS',['name','subcategory'],data)


def GetDataSourceProductos(conn):
    pathData="/workspaces/workspacepy01/proyecto/files/data.xls"
    df=pd.read_excel(pathData,sheet_name="Orders")
    df_products=df[['Product ID','Product Name','Category']].dropna().drop_duplicates()
    df_categoria=pd.read_sql_query("SELECT id,name FROM CATEGORIAS",conn)
    #df_newProducts=df_products.merge(df_categoria,how="left",left_on='Category',right_on='name')
    #print(df_newProducts.head())
    df_newProducts=df_products.merge(df_categoria,how="left",left_on='Category',right_on='name')
    df_newProducts=df_newProducts[['Product ID','Product Name','id']]
    df_newProducts=[tuple(x) for x in df_products.to_records(index=False)]
    return df_newProducts

def createTableProducts(conn:Connection):
    productos=Productos()
    productos.create_table(conn)

def InsertManyProducts(bd:Database,data):
    bd.insert_many('PRODUCTOS',['product_id','name','category_id'],data)


def GetDatasourceOrders(conn):
    pathData="/workspaces/workspacepy01/proyecto/files/data.xls"
    df=pd.read_excel(pathData,sheet_name="Orders")
    df_products=pd.read_sql_query("SELECT id,name,product_id FROM PRODUCTOS",conn)
    df_orders=df[['Order ID','Postal Code','Product ID','Sales','Quantity','Discount','Profit','Shipping Cost','Order Priority']].dropna().drop_duplicates()
    df_orders['Postal Code'] = df_orders['Postal Code'].astype(str)
    print('shape orders',df_orders.shape)
    df_newOrders=df_orders.merge(df_products,how="left",left_on="Product ID",right_on="product_id")
    df_newOrders=df_newOrders.drop_duplicates()
    print('shape orders 1',df_newOrders.shape)
    df_newOrders=df_newOrders[['Order ID','Postal Code','id','Sales','Quantity','Discount','Profit','Shipping Cost','Order Priority']]
    list_tuples=[tuple(x) for x in df_newOrders.to_records(index=False)]
    return list_tuples
    
    return list_tuples

def createTableVentas(conn):
    ventas=Ventas()
    ventas.create_table(conn)

def insertManyVentas(bd:Database,data):
    bd.insert_many('VENTAS',['order_id','postal_code','product_id','sales_amount','quantity','discount','profit','shipping_cost','order_priority'],data)


def GetDatasourceFecha():
    pathData = "/workspaces/workspacepy01/proyecto/files/data.xls"
    df = pd.read_excel(pathData, sheet_name="Orders")
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce').dt.strftime('%Y-%m-%d')
    df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce').dt.strftime('%Y-%m-%d')
    df_fecha = df[['Order ID', 'Order Date','Ship Date']].dropna().drop_duplicates()
    df_fecha.rename(columns={'Order ID': 'order_id', 'Order Date': 'order_date', 'Ship Date': 'ship_date'}, inplace=True)
    list_tuples = [tuple(x) for x in df_fecha.to_records(index=False)]
    return list_tuples

def createTableFecha(conn: Connection):
    fecha = Fecha()  
    fecha.create_table(conn)

def InsertManyFecha(bd: Database, data):
    bd.insert_many('FECHA', ['order_id', 'order_date', 'ship_date'], data)
