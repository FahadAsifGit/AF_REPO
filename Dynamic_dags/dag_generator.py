from airflow import DAG
import dagfactory

dag_factory = dagfactory.DagFactory("./dag_config.yaml")

dag_factory.clean_dags(globals())
dag_factory.generate_dags(globals())