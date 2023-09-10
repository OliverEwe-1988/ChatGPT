#include "direktchatgpt.h"
#include "ui_direktchatgpt.h"

DirektChatGPT::DirektChatGPT(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::DirektChatGPT)
{
    ui->setupUi(this),
    connect(ui->pushButton, &QPushButton::clicked, this, &::DirektChatGPT::on_pushButton_clicked);
    }

DirektChatGPT::~DirektChatGPT()
{
    delete ui;
}

void DirektChatGPT::on_pushButton_clicked()
{

}

