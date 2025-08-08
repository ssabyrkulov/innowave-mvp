from alembic import op
import sqlalchemy as sa

# ID этой миграции
revision = "0001_init"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Таблица пользователей
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String(255), nullable=False, unique=True, index=True),
        sa.Column("password_hash", sa.String(255), nullable=False),
        sa.Column("full_name", sa.String(255), nullable=True),
        sa.Column("is_active", sa.Boolean, nullable=False, server_default=sa.sql.expression.true()),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    # Таблица компаний
    op.create_table(
        "companies",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(255), nullable=False, index=True),
        sa.Column("inn", sa.String(50), nullable=True),
        sa.Column("country", sa.String(10), nullable=True),
    )
    op.create_index("ix_companies_name", "companies", ["name"], unique=False)

def downgrade():
    op.drop_index("ix_companies_name", table_name="companies")
    op.drop_table("companies")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
