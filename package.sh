set -e

if [ "$1" == "--deps" ]; then
  echo "Rebuilding dependencies layer"

  rm -rf ./layer/*

  pip3 freeze > ./layer/requirements.txt
  sam build -b ./build --use-container -m ./layer/requirements.txt

  # Move dependencies into the layer.
  mkdir ./layer/python
  mv ./build/CloudTrailToLineage/* ./layer/python
  rm -rf ./layer/python/src

  rm -rf ./build

fi;

echo "Packaging app"
aws cloudformation package --template-file template.yaml --s3-bucket lineage-artifacts-2020 --output-template-file packaged.yaml

echo "Deploying app"
aws cloudformation deploy --template-file packaged.yaml --stack-name CloudTrailToLineage --capabilities CAPABILITY_IAM