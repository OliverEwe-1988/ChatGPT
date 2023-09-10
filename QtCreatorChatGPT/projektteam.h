#ifndef PROJEKTTEAM_H
#define PROJEKTTEAM_H

#include <QMainWindow>

namespace Ui {
class Projektteam;
}

class Projektteam : public QMainWindow
{
    Q_OBJECT

public:
    explicit Projektteam(QWidget *parent = nullptr);
    ~Projektteam();

private:
    Ui::Projektteam *ui;
};

#endif // PROJEKTTEAM_H
