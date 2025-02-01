# Devsu Technical Test - API REST

Este proyecto implementa una API REST con Django y se despliega en AWS EKS usando Terraform para la infraestructura y GitHub Actions para CI/CD.

## Arquitectura

### Diagrama de Infraestructura
mermaid
graph TB
Internet((Internet)) --> ALB[Application Load Balancer]
subgraph VPC
subgraph Public Subnets
ALB --> |Route traffic| NG[NAT Gateway]
end
subgraph Private Subnets
subgraph EKS Cluster
NG --> |Internet access| Node1[Worker Node 1]
NG --> |Internet access| Node2[Worker Node 2]
subgraph Pods
Node1 --> Pod1[Django API Pod 1]
Node1 --> Pod2[Django API Pod 2]
Node2 --> Pod3[Django API Pod 3]
end
end
end
end
CW[CloudWatch] --> |Logs & Metrics| EKS Cluster


### Diagrama de CI/CD

mermaid
graph LR
Dev[Developer] -->|Push| Git[GitHub Repo]
Git -->|Trigger| GHA[GitHub Actions]
subgraph CI/CD Pipeline
GHA -->|Run| Tests[Django Tests]
Tests -->|If Pass| Build[Docker Build]
end


## Componentes Principales

### 1. API REST (Django)
- Framework: Django REST Framework
- Base de datos: SQLite (desarrollo)
- Endpoints:
  - GET /api/users/
  - POST /api/users/
  - GET /api/users/{id}/

### 2. Infraestructura AWS (Terraform)
- **VPC**
  - 3 subnets públicas
  - 3 subnets privadas
  - NAT Gateway
  - Internet Gateway

- **EKS Cluster**
  - Versión: 1.27
  - 2 nodos t3.medium
  - Auto-scaling: 1-3 nodos

- **Application Load Balancer**
  - Health checks
  - Target Groups
  - Security Groups

- **CloudWatch**
  - Logs del cluster
  - Logs de aplicación
  - Dashboard personalizado
  - Alarmas de CPU y errores

### 3. CI/CD (GitHub Actions)
- **Test Stage**
  - Ejecuta pruebas unitarias
  - Verifica migraciones
  - Validación de código

- **Build Stage**
  - Construye imagen Docker
  - Solo en rama main

## Configuración y Despliegue

### Requisitos Previos

bash
AWS CLI
aws configure
Terraform
terraform -v
kubectl
kubectl version


### Despliegue de Infraestructura

bash
cd terraform
terraform init
terraform plan
terraform apply

### Configuración de kubectl

bash
aws eks update-kubeconfig --region us-west-2 --name devsu-eks-cluster


### Despliegue de la Aplicación

bash
kubectl apply -f k8s/


## Monitoreo y Logs

### CloudWatch Dashboard
- Métricas de ALB
  - Request Count
  - Response Time
  - Error Rates

- Métricas de EKS
  - CPU Utilization
  - Memory Usage
  - Node Status

### Alarmas Configuradas
- CPU Usage > 80%
- Error Rate (5XX) > 10 en 5 minutos

## Seguridad

### Network
- VPC con subnets públicas y privadas
- Nodos EKS en subnets privadas
- ALB en subnets públicas
- Security Groups restrictivos

### IAM
- Roles mínimos necesarios
- Políticas específicas por servicio

## Desarrollo Local

### Requisitos
- Python 3.11
- Docker
- Make (opcional)

### Comandos

bash
Instalar dependencias
pip install -r requirements.txt
Ejecutar tests
python manage.py test
Ejecutar servidor local
python manage.py runserver


## API Endpoints

### GET /api/users/

json
[
{
"id": 1,
"dni": "12345",
"name": "John Doe"
}
]


### POST /api/users/

json
{
"dni": "12345",
"name": "John Doe"
}


### GET /api/users/{id}/

json
{
"id": 1,
"dni": "12345",
"name": "John Doe"
}



## Contribución
1. Fork el repositorio
2. Crea una rama (`git checkout -b feature/amazing`)
3. Commit tus cambios (`git commit -m 'Add amazing feature'`)
4. Push a la rama (`git push origin feature/amazing`)
5. Abre un Pull Request

## Licencia
Este proyecto está bajo la licencia MIT.