#ifndef DIREKTCHATGPT_H
#define DIREKTCHATGPT_H

#include <QMainWindow>

namespace Ui {
class DirektChatGPT;
}

class DirektChatGPT : public QMainWindow
{
    Q_OBJECT

public:
    explicit DirektChatGPT(QWidget *parent = nullptr);
    ~DirektChatGPT();

private:
    Ui::DirektChatGPT *ui;
};

#endif // DIREKTCHATGPT_H
