#include "tablechatgpt.h"
#include "ui_tablechatgpt.h"

TableChatGPT::TableChatGPT(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::TableChatGPT)
{
    ui->setupUi(this);
}

TableChatGPT::~TableChatGPT()
{
    delete ui;
}
