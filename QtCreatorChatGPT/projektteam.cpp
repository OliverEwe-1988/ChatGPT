#include "projektteam.h"
#include "ui_projektteam.h"

Projektteam::Projektteam(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Projektteam)
{
    ui->setupUi(this);
}

Projektteam::~Projektteam()
{
    delete ui;
}
