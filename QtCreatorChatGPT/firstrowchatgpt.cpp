#include "firstrowchatgpt.h"
#include "ui_firstrowchatgpt.h"

FirstRowChatGPT::FirstRowChatGPT(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::FirstRowChatGPT)
{
    ui->setupUi(this);
}

FirstRowChatGPT::~FirstRowChatGPT()
{
    delete ui;
}
