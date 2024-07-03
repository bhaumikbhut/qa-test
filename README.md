# qa-test

**Kubernetes Deployment:**

Deploy the services to a local Kubernetes cluster (e.g., Minikube or Kind).

**Verification:**

- Ensure the frontend service can successfully communicate with the backend service.
- Verify that accessing the frontend URL displays the greeting message fetched from the backend.

**Automated Testing:**

- Write a simple test script (using a tool of your choice) to verify the integration between the frontend and backend services.
- The test should check that the frontend correctly displays the message returned by the backend.

**Documentation:**

- Provide a README file with instructions on how to set up and run the automated tests script.

**Deliverables:**
- Test script for automated testing.
- README file with setup and execution instructions.

**Github repo should be Public**


**How to Setup Repo**

1. Clone this repo 
2. Download minikube from [here](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Fx86-64%2Fstable%2Fbinary+download)
3. Build your Docker image for backend

    docker build -t backend-app:v1 .

4. Build your Docker image for frontend 

    docker build -t frontend-app:v1 .

5. Apply the Deployment

    kubectl apply -f {path of backend-deployment.yaml}

    kubectl apply -f {path of frontend-deployment.yaml}

6. Expose Your Service

7. Apply the services

    kubectl apply -f {path of backend-service.yaml}

    kubectl apply -f {path of frontend-service.yaml}

8. Access Application

    minikube service frontend-service

    minikube service backend-service
    

**How to Run Test**

1. Go to IntegtationTest 
2. npm i
3. npx playwright test
4. npx playwright show-report