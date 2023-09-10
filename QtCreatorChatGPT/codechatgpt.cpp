#include "codechatgpt.h"
#include "ui_codechatgpt.h"

CodeChatGPT::CodeChatGPT(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::CodeChatGPT)
{
    ui->setupUi(this);
}

CodeChatGPT::~CodeChatGPT()
{
    delete ui;
}
