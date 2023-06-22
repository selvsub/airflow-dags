from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "hello-0622161220",
}

dag = DAG(
    "hello-0622161220",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using hello.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_aa26509b_2068_41b0_a363_aa53261a63c1 = NotebookOp(
    name="hello",
    namespace="ml-workshop",
    task_id="hello",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/hello.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello-0622161220",
    cos_dependencies_archive="hello-aa26509b-2068-41b0-a363-aa53261a63c1.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_aa26509b_2068_41b0_a363_aa53261a63c1.image_pull_policy = "IfNotPresent"


notebook_op_e3a3f104_df79_44b6_acec_eecbb532e43e = NotebookOp(
    name="world",
    namespace="ml-workshop",
    task_id="world",
    notebook="Machine-Learning-on-Kubernetes/Chapter07/model_deploy_pipeline/world.py",
    cos_endpoint="http://minio-ml-workshop:9000/",
    cos_bucket="airflow",
    cos_directory="hello-0622161220",
    cos_dependencies_archive="world-e3a3f104-df79-44b6-acec-eecbb532e43e.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_e3a3f104_df79_44b6_acec_eecbb532e43e.image_pull_policy = "IfNotPresent"

(
    notebook_op_e3a3f104_df79_44b6_acec_eecbb532e43e
    << notebook_op_aa26509b_2068_41b0_a363_aa53261a63c1
)
