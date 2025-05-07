get-image() {
  ssh $PROJECT_USER@$PROJECT_HOST -c "kubectl describe pod -n dev $(kubectl get pods -n dev | grep hamster.*Running | awk '{print $1}') | grep Image | awk 'NR==1 {print $2}'"
}
