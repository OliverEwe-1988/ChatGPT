#ifndef FIRSTROWCHATGPT_H
#define FIRSTROWCHATGPT_H

#include <QMainWindow>

namespace Ui {
class FirstRowChatGPT;
}

class FirstRowChatGPT : public QMainWindow
{
    Q_OBJECT

public:
    explicit FirstRowChatGPT(QWidget *parent = nullptr);
    ~FirstRowChatGPT();

private:
    Ui::FirstRowChatGPT *ui;
};

#endif // FIRSTROWCHATGPT_H
