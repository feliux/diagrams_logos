from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from urllib.request import urlretrieve


with Diagram("MOI", show=False, filename="custom_remote", direction="LR"):

    murex_icon = "ControlM.jpg"
    murex_path = f"https://github.com/feliux/diagrams_logos/blob/master/logos/{murex_icon}"
    urlretrieve(murex_path, murex_icon)
    murex = Custom("Murex", murex_icon)

    with Cluster("Azure"):
        
        scality_icon = "Scality.webp"
        scality_path = f"https://github.com/feliux/diagrams_logos/blob/master/logos/{scality_icon}"
        urlretrieve(scality_path, scality_icon)
        databricks = Custom("Databricks", scality_path)

        spark_icon = "Spark.png"
        spark_path = f"https://github.com/feliux/diagrams_logos/blob/master/logos/{spark_icon}"
        urlretrieve(spark_path, spark_icon)
        spark = Custom("Spark", spark_icon)

    murex >> databricks
    murex >> spark