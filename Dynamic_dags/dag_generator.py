from airflow import DAG
import dagfactory

dag_factory = dagfactory.DagFactory("/home/runner/work/AF_REPO/AF_REPO/Dynamic_dags/dag_config.yaml")

dag_factory.clean_dags(globals())
dag_factory.generate_dags(globals())
