#ifndef CODECHATGPT_H
#define CODECHATGPT_H

#include <QMainWindow>

namespace Ui {
class CodeChatGPT;
}

class CodeChatGPT : public QMainWindow
{
    Q_OBJECT

public:
    explicit CodeChatGPT(QWidget *parent = nullptr);
    ~CodeChatGPT();

private:
    Ui::CodeChatGPT *ui;
};

#endif // CODECHATGPT_H
