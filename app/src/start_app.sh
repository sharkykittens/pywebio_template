sleep 5 #wait for postgres to be ready
if [ "$RESET_DATABASE" = "true" ]; then
    echo "Resetting Database..."
    prisma migrate reset --force
fi

prisma generate
prisma db push
python3 main.py