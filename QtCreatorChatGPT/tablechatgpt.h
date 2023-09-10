#ifndef TABLECHATGPT_H
#define TABLECHATGPT_H

#include <QMainWindow>

namespace Ui {
class TableChatGPT;
}

class TableChatGPT : public QMainWindow
{
    Q_OBJECT

public:
    explicit TableChatGPT(QWidget *parent = nullptr);
    ~TableChatGPT();

private:
    Ui::TableChatGPT *ui;
};

#endif // TABLECHATGPT_H
